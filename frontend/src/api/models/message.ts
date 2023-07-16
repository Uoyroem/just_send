import { User } from "./user";

export interface Message {
    id: number;
    chat: number;
    sender?: User;
    message: string;
    created_at: string;
    updated_at: string;
}