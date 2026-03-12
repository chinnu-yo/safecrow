import json
from google import genai
from google.genai import types

from app.core.config import settings

class AIService:
    def __init__(self):
        self._client = None
        self.model_id = "gemini-2.5-flash"
        
    @property
    def client(self):
        if self._client is None:
            if not settings.GEMINI_API_KEY:
                # Warning: Gemini API functionality will fail if api_key is empty.
                pass
            self._client = genai.Client(api_key=settings.GEMINI_API_KEY)
        return self._client

    def generate_conditions(self, description: str) -> str:
        """
        Takes a description of a gig/transaction and generates clear, objective criteria 
        for its completion.
        """
        prompt = f"""
        You are an expert escrow agent and contract writer.
        Based on the following transaction description, generate a detailed, objective, 
        and verifiable list of conditions that must be met for the transaction to be considered complete.
        
        Description: "{description}"
        
        Return the conditions as a clear bulleted list or numbered list. 
        Focus heavily on measurable deliverables.
        """
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
        )
        return response.text.strip()

    def verify_submission(self, conditions: str, submission: str) -> dict:
        """
        Evaluates a submission against the agreed upon conditions.
        Returns a dict with 'ai_score' (0.0 to 1.0) and 'ai_verdict' (explanation).
        """
        prompt = f"""
        You are an impartial AI judge evaluating whether a job has been completed.
        
        Agreed upon conditions:
        "{conditions}"
        
        Seller's submission evidence:
        "{submission}"
        
        Evaluate the submission against the conditions.
        Provide a JSON response with two keys:
        1. "score": A float between 0.0 and 1.0 representing how well the submission meets the conditions (1.0 = perfect match).
        2. "verdict": A brief string explaining your reasoning.
        """
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        try:
            result = json.loads(response.text)
            return {
                "ai_score": float(result.get("score", 0.0)),
                "ai_verdict": str(result.get("verdict", "No verdict provided."))
            }
        except json.JSONDecodeError:
            # Fallback if the AI doesn't return valid JSON
            return {
                "ai_score": 0.0,
                "ai_verdict": f"Failed to parse AI response. Raw output: {response.text}"
            }

ai_service = AIService()
