"use client";

import { create } from "zustand";

type User = {
  id: string;
  userName: string;
};

type InitialState = {
  isAuthentication: boolean;
  user: User;
};

type UseAuth = {
  initialState: InitialState;
  Initialize: (data: User) => void;
  Logout: () => void;
  Login: (token: string) => void;
};

const initialState: InitialState = {
  isAuthentication: false,
  user: {
    id: "0",
    userName: "",
  },
};

export const useAuth = create<UseAuth>((set, get) => ({
  initialState,
  Initialize: (data) => {
    const token = sessionStorage.getItem("accessToken");

    if (token !== null && data) {
      set({
        initialState: {
          isAuthentication: true,
          user: data,
        },
      });
    } else {
      get().Logout();
    }
  },
  Login: (token) => {
    sessionStorage.setItem("accessToken", token);
    set({
      initialState: {
        ...initialState,
        isAuthentication: true,
      },
    });
  },
  Logout: () => {
    set({
      initialState,
    });
    sessionStorage.removeItem("accessToken");
  },
}));
