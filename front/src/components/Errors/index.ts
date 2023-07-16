import { BadRequest } from "./400";
import { Unauthorized } from "./401";
import { Forbidden } from "./403";
import { NotFound } from "./404";
import { InternalServerError } from "./500";
import { NotImplemented } from "./501";
import { Root } from "./Root";

export const Errors = {
  Root,
  BadRequest,
  Unauthorized,
  Forbidden,
  NotFound,
  InternalServerError,
  NotImplemented,
};
