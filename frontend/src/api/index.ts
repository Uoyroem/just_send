
import { Chat, Message } from './models';

const API_URL = 'http://localhost:8001/api';
function getChatListUrl() {
    return `${API_URL}/chats.json`;
}
function getMessageListUrl(chatId: number) {
    return `${API_URL}/chats/${chatId}/messages.json`;
}

export default class Api {
    static async chats(): Promise<Chat[]> {
        const response = await fetch(getChatListUrl());
        return await response.json();
    }

    static async messages(chatId: number): Promise<Message[]> {
        const response = await fetch(getMessageListUrl(chatId));
        return await response.json();
    }

    static async sendMessage(chatId: number, message: string): Promise<Message> {
        const response = await fetch(getMessageListUrl(chatId), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        return await response.json();
    }
}
