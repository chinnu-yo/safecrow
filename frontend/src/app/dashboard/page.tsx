import Link from "next/link";
import { PlusCircle, Search } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { mockEscrows, EscrowStatus } from "@/lib/types";

const getStatusBadge = (status: EscrowStatus) => {
  switch (status) {
    case "PENDING_FUNDING":
      return <Badge variant="outline" className="text-yellow-500 border-yellow-500/50">Pending Funding</Badge>;
    case "FUNDED":
      return <Badge variant="outline" className="text-blue-500 border-blue-500/50">Funded</Badge>;
    case "IN_PROGRESS":
      return <Badge variant="default" className="bg-primary/20 text-primary hover:bg-primary/30">In Progress</Badge>;
    case "IN_DISPUTE":
      return <Badge variant="destructive" className="bg-destructive/20 text-destructive border-transparent hover:bg-destructive/30">In Dispute</Badge>;
    case "RESOLVED":
      return <Badge variant="outline" className="text-purple-500 border-purple-500/50">Resolved</Badge>;
    case "COMPLETED":
      return <Badge variant="outline" className="text-green-500 border-green-500/50">Completed</Badge>;
    case "CANCELLED":
      return <Badge variant="secondary" className="text-muted-foreground">Cancelled</Badge>;
    default:
      return <Badge variant="outline">{status}</Badge>;
  }
};

export default function Dashboard() {
  return (
    <div className="flex-1 space-y-4 p-8 pt-6 container max-w-screen-2xl mx-auto">
      <div className="flex items-center justify-between space-y-2">
        <h2 className="text-3xl font-bold tracking-tight">Dashboard</h2>
        <div className="flex items-center space-x-2">
          <Link href="/escrow/new">
            <Button>
              <PlusCircle className="mr-2 h-4 w-4" />
              New Escrow
            </Button>
          </Link>
        </div>
      </div>
      
      <div className="flex items-center space-x-2 pb-4">
        <div className="relative flex-1 md:max-w-sm">
          <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
          <Input
            type="search"
            placeholder="Search escrows..."
            className="pl-8 bg-background"
          />
        </div>
      </div>
      
      <Card className="border-border/50 bg-card/50 backdrop-blur">
        <CardHeader>
          <CardTitle>Recent Escrows</CardTitle>
          <CardDescription>
            You have {mockEscrows.length} active escrows.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow className="border-border/50 hover:bg-transparent">
                <TableHead>Title</TableHead>
                <TableHead>Amount</TableHead>
                <TableHead>Status</TableHead>
                <TableHead className="hidden md:table-cell">Due Date</TableHead>
                <TableHead className="text-right">Action</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {mockEscrows.map((escrow) => (
                <TableRow key={escrow.id} className="border-border/50">
                  <TableCell className="font-medium">
                    <div className="flex flex-col">
                      <span>{escrow.title}</span>
                      <span className="text-xs text-muted-foreground hidden sm:inline-block">ID: {escrow.id}</span>
                    </div>
                  </TableCell>
                  <TableCell>{escrow.amount} {escrow.currency}</TableCell>
                  <TableCell>{getStatusBadge(escrow.status)}</TableCell>
                  <TableCell className="hidden md:table-cell text-muted-foreground">
                    {new Date(escrow.due_date).toLocaleDateString()}
                  </TableCell>
                  <TableCell className="text-right">
                    <Link href={`/escrow/${escrow.id}`}>
                      <Button variant="ghost" size="sm" className="hover:bg-primary/10 hover:text-primary">
                        View Details
                      </Button>
                    </Link>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
