import { AuthGuard } from "../../guards/AuthGuard";

export default function AuthenticatorLayoutComponent({
  children,
}: {
  children: React.ReactNode;
}) {
  return <AuthGuard>{children}</AuthGuard>;
}
