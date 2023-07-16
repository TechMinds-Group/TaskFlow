import axios from "axios";

export const backConnection: any = axios.create({
  baseURL: process.env.NEXT_PUBLIC_BASE_URL,
});
