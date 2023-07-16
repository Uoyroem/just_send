import React from 'react';
import './Message.sass';
import * as models from '../api/models';


interface MessageProps {
    message: models.Message;
}

export default function Message({ message }: MessageProps) {
    return (<div>
        <div>{message.sender?.username ?? "Anonymous"}</div>
        <span>{message.message}</span>
    </div>)
}