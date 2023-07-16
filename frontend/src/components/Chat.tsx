import React from 'react';

import * as models from '../api/models';
import './Chat.sass';

interface ChatProps {
    chat: models.Chat;
    selected: boolean;
    onClick?: (chat: models.Chat) => void;
}

export default function Chat({ chat, selected, onClick }: ChatProps) {
    return (<div className={selected ? "chat chat_selected" : "chat"} onClick={() => onClick?.(chat)}>
        <img className="chat__thumbnail" src={chat.thumbnail} alt="" />
        <span className="chat__title">{chat.title}</span>
    </div>);
}