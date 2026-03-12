"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ShieldCheck } from "lucide-react";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 max-w-screen-2xl items-center mx-auto px-4 md:px-8">
        <Link href="/" className="mr-6 flex items-center space-x-2">
          <ShieldCheck className="h-6 w-6 text-primary" />
          <span className="font-bold sm:inline-block">SafeCrow</span>
        </Link>
        <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
          <nav className="flex items-center space-x-6 text-sm font-medium">
            <Link
              href="/dashboard"
              className="transition-colors hover:text-foreground/80 text-foreground/60"
            >
              Dashboard
            </Link>
            <Link
              href="/escrow/new"
              className="transition-colors hover:text-foreground/80 text-foreground/60"
            >
              Create Escrow
            </Link>
          </nav>
          <div className="flex items-center ml-4">
            <Button variant="default" className="hidden md:flex">
              Connect Wallet
            </Button>
            <Button variant="outline" className="flex md:hidden ml-2">
              Menu
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
}
