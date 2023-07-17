"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { useUserMe } from "../queries/User/useUserMe";
import { useAuth } from "../store/useAuth";

export const AuthGuard = ({ children }: { children: any }) => {
  const { initialState, Initialize } = useAuth();
  const router = useRouter();
  const { data, isLoading } = useUserMe();

  useEffect(() => {
    if (data) {
      Initialize(data);
    }
  }, [data, Initialize]);

  useEffect(() => {
    if (!initialState.isAuthentication) {
      router.push("/login");
    }
  }, [initialState.isAuthentication, router]);

  return initialState.isAuthentication && children;
};
