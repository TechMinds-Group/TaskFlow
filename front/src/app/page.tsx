"use client";
import { useRouter } from "next/navigation";
import { QueryClientProvider } from "react-query";
import { queryClient } from "../services/queryClient";

export default function Home() {
  const router = useRouter();

  return (
    <QueryClientProvider client={queryClient}>
      <main>
        <button onClick={() => router.push("login")}>clique</button>
      </main>
    </QueryClientProvider>
  );
}
