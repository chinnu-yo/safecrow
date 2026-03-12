"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { ArrowLeft, Save, Sparkles } from "lucide-react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";

export default function NewEscrowPage() {
  const router = useRouter();
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    // Simulate API call
    setTimeout(() => {
      setIsSubmitting(false);
      router.push("/dashboard");
    }, 1500);
  };

  return (
    <div className="container max-w-3xl mx-auto p-4 py-8">
      <Button 
        variant="ghost" 
        className="mb-6 -ml-4 text-muted-foreground hover:text-foreground"
        onClick={() => router.back()}
      >
        <ArrowLeft className="mr-2 h-4 w-4" />
        Back to Dashboard
      </Button>

      <Card className="border-border/50 bg-card/60 backdrop-blur shadow-xl">
        <form onSubmit={handleSubmit}>
          <CardHeader className="space-y-1">
            <div className="flex items-center justify-between">
              <CardTitle className="text-2xl font-bold">Create Escrow</CardTitle>
              <div className="flex items-center px-3 py-1 bg-primary/10 text-primary rounded-full text-xs font-semibold">
                <Sparkles className="h-3 w-3 mr-1" />
                AI Arbitrated
              </div>
            </div>
            <CardDescription>
              Define the specific terms of the transaction. Clearer terms lead to better AI arbitration if a dispute arises.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="space-y-2">
              <Label htmlFor="title">Transaction Title</Label>
              <Input id="title" placeholder="e.g. Website Development" required className="bg-background" />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="amount">Amount</Label>
                <div className="relative">
                  <Input id="amount" type="number" step="0.01" placeholder="0.00" required className="bg-background pr-16" />
                  <div className="absolute inset-y-0 right-0 flex items-center px-3 pointer-events-none text-muted-foreground border-l border-border bg-muted/50 rounded-r-md">
                    USDC
                  </div>
                </div>
              </div>
              <div className="space-y-2">
                <Label htmlFor="dueDate">Due Date</Label>
                <Input id="dueDate" type="date" required className="bg-background" />
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="buyer">Buyer Address (or Email)</Label>
                <Input id="buyer" placeholder="0x..." required className="bg-background" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="seller">Seller Address (or Email)</Label>
                <Input id="seller" placeholder="0x..." required className="bg-background" />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="terms">Detailed Terms & Deliverables</Label>
              <Textarea
                id="terms"
                placeholder="Describe exactly what needs to be delivered, formatted clearly for the AI arbiter..."
                className="min-h-[150px] bg-background resize-y"
                required
              />
              <p className="text-xs text-muted-foreground">
                In case of a dispute, Gemini AI will analyze these terms line by line against the submitted evidence.
              </p>
            </div>
          </CardContent>
          <CardFooter className="flex justify-end gap-4 border-t border-border/50 bg-muted/20 px-6 py-4">
            <Button type="button" variant="ghost" onClick={() => router.back()}>
              Cancel
            </Button>
            <Button type="submit" disabled={isSubmitting} className="min-w-[150px]">
              {isSubmitting ? (
                <>Processing...</>
              ) : (
                <>
                  <Save className="mr-2 h-4 w-4" /> Deploy Escrow
                </>
              )}
            </Button>
          </CardFooter>
        </form>
      </Card>
    </div>
  );
}
