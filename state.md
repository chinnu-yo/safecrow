# Global State & Schema

## Database Schema (PostgreSQL)
### Users Table
- `id`: Integer (Primary Key)
- `username`: String
- `wallet_balance`: Float (Default: 1000.0)

### EscrowTransactions Table
- `id`: UUID
- `buyer_id`: Integer (FK Users)
- `seller_id`: Integer (FK Users)
- `amount`: Float
- `status`: Enum (PENDING, FUNDED, COMPLETED, DISPUTED, RELEASED)
- `conditions`: JSONB (Array of strings)
- `submission_text`: Text (Optional)
- `ai_score`: Integer (0-100)
- `ai_verdict`: Text

## API Endpoints (Contract)
1. `POST /api/agreement`: Input `{description}` -> Output `{"conditions": []}`
2. `POST /api/escrow/create`: Create record with status PENDING.
3. `POST /api/escrow/fund`: Change status to FUNDED.
4. `POST /api/verify`: Input `{escrow_id, submission}` -> Output `{"satisfied": bool, "score": int, "reason": str}`
5.