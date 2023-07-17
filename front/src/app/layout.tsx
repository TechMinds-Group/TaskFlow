"use client";

import { QueryClientProvider } from "@tanstack/react-query";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { useNProgress } from "../hooks/useNProgress";
import { queryClient } from "../services/queryClient";
import "../styles/globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "TaskFlow",
  description: "Desenvolvido por TechMinds",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  useNProgress();

  return (
    <html lang="ptbr">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/logo_taskflow_without_text.svg" />
        <title>TaskFlow</title>
      </head>
      <body className={inter.className}>
        <QueryClientProvider client={queryClient}>
          {children}
        </QueryClientProvider>
      </body>
    </html>
  );
}
