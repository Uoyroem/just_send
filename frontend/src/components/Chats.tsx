import React from 'react';
import * as models from '../api/models';
import Api from '../api';
import Chat from './Chat';
import Message from './Message';
import './Chats.sass';

export default function Chats() {
    const [selectedChat, setSelectedChat] = React.useState<number | null>(null);
    const [chats, setChats] = React.useState<models.Chat[]>([]);
    const [messages, setMessages] = React.useState<models.Message[]>([]);
    const [message, setMessage] = React.useState<string>('');

    React.useEffect(() => {
        Api.chats().then(setChats);
    }, []);

    React.useEffect(() => {
        if (selectedChat != null) {
            Api.messages(selectedChat).then(setMessages);
        }
    }, [selectedChat]);

    const sendMessage = () => {
        if (selectedChat != null && message != '') {
            Api.sendMessage(selectedChat, message).then(message => {
                setMessages(messages => [...messages, message]);
            });
            setMessage('');
        }
    };

    return (
        <div className="chats-grid">
            <div className="chats-grid__messages">
                {messages.map(message => {
                    return <Message message={message} />
                })}
            </div>
            <div className="chats-grid__message-input-container">
                <input
                    className="input chats-grid__message-input" type="text"
                    value={message}
                    onChange={event => setMessage(event.target.value)}
                    onKeyPress={event => event.key === 'Enter' && sendMessage()}
                />
                <button className="button" onClick={sendMessage}>Отправить</button>
            </div>

            <div className="chats-grid__chats">
                {chats.map(chat => {
                    return <Chat chat={chat} key={chat.id} selected={chat.id === selectedChat} onClick={() => setSelectedChat(chat.id)} />
                })}
            </div>
        </div>
    )
}

