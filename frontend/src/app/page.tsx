import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowRight, Shield, Zap, Lock } from "lucide-react";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[calc(100vh-4rem)]">
      {/* Hero Section */}
      <section className="w-full flex flex-col items-center justify-center text-center px-4 py-24 md:py-32 lg:py-40 relative overflow-hidden">
        {/* Abstract background gradient */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-primary/20 blur-[120px] rounded-full pointer-events-none -z-10" />
        
        <h1 className="text-4xl md:text-6xl lg:text-7xl font-extrabold tracking-tight max-w-4xl bg-clip-text text-transparent bg-gradient-to-r from-white to-white/60 mb-6">
          AI-Powered Trustless <span className="text-primary">Escrow</span>
        </h1>
        <p className="text-lg md:text-xl text-muted-foreground max-w-2xl mb-10 leading-relaxed">
          Secure your transactions with intelligent, automated escrow services. Protect buyers and sellers using advanced AI arbitration and immutable smart contracts.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
          <Link href="/escrow/new">
            <Button size="lg" className="w-full sm:w-auto font-semibold gap-2">
              Start Transaction <ArrowRight className="h-4 w-4" />
            </Button>
          </Link>
          <Link href="/dashboard">
            <Button size="lg" variant="secondary" className="w-full sm:w-auto font-semibold">
              View Dashboard
            </Button>
          </Link>
        </div>
      </section>

      {/* Features Section */}
      <section className="w-full max-w-6xl mx-auto px-4 py-20 bg-background">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="flex flex-col items-center text-center p-6 rounded-2xl border border-border/50 bg-card hover:border-primary/50 transition-colors duration-300">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center mb-6">
              <Shield className="h-6 w-6 text-primary" />
            </div>
            <h3 className="text-xl font-semibold mb-3">Absolute Security</h3>
            <p className="text-muted-foreground text-sm leading-relaxed">
              Funds are locked cryptographically until all conditions are unequivocally met by both parties.
            </p>
          </div>
          <div className="flex flex-col items-center text-center p-6 rounded-2xl border border-border/50 bg-card hover:border-primary/50 transition-colors duration-300">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center mb-6">
              <Zap className="h-6 w-6 text-primary" />
            </div>
            <h3 className="text-xl font-semibold mb-3">AI Arbitration</h3>
            <p className="text-muted-foreground text-sm leading-relaxed">
              Instant, unbiased dispute resolution powered by Gemini 3 Flash analyzing the original agreement.
            </p>
          </div>
          <div className="flex flex-col items-center text-center p-6 rounded-2xl border border-border/50 bg-card hover:border-primary/50 transition-colors duration-300">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center mb-6">
              <Lock className="h-6 w-6 text-primary" />
            </div>
            <h3 className="text-xl font-semibold mb-3">Milestone Releases</h3>
            <p className="text-muted-foreground text-sm leading-relaxed">
              Break down complex projects into payable milestones to protect cash flow and minimize risk.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
