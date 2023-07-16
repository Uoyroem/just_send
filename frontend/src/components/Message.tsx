import React from 'react';
import './Message.sass';
import * as models from '../api/models';


interface MessageProps {
    message: models.Message;
}

export default function Message({ message }: MessageProps) {
    return (<div className="message">
        <div className="message__header">
            <div className="message__sender">
                {message.sender?.username ?? "Anonymous"}
            </div>
            <div className="message__updated-at">
                {new Date(message.updated_at).toLocaleDateString(undefined, { year: 'numeric', hour: 'numeric', minute: 'numeric', month: 'numeric', day: 'numeric' })}
            </div>
        </div>
        <span>{message.message}</span>
    </div>)
}