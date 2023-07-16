import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function AuthenticatorLayoutComponent({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ptbr">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
