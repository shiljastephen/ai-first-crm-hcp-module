import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import api from "../api/api";
import { setInteraction } from "../features/interaction/interactionSlice";

import "../styles/chat.css";

function ChatPanel() {

    const dispatch = useDispatch();

    const currentInteraction = useSelector(
        (state) => state.interaction.data
    );

    const [message, setMessage] = useState("");

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    const sendMessage = async () => {

        if (!message.trim()) return;

        const userMessage = {
            role: "user",
            content: message
        };

        setMessages(prev => [...prev, userMessage]);

        setLoading(true);

        try {

            const response = await api.post("/ai/chat", {
                message,
                current_interaction: currentInteraction
            });

            let assistantReply = "";

            switch (response.data.tool) {

                case "log":

                    dispatch(
                        setInteraction(response.data.data)
                    );

                    assistantReply =
                        "✅ Interaction logged successfully.\n\nThe interaction has been extracted and the form has been populated.";

                    break;

                case "edit":

                    dispatch(
                        setInteraction(response.data.data)
                    );

                    assistantReply =
                        "✏️ Interaction updated successfully.";

                    break;

                case "summary":

                    assistantReply =
                        "📝 Summary\n\n" +
                        response.data.summary;

                    break;

                case "followup":

                    assistantReply =
                        "📅 Follow-up Suggestion\n\n" +
                        response.data.follow_up;

                    break;

                case "recommendation":

                    assistantReply =
                        "💡 Recommendation\n\n" +
                        response.data.recommendation;

                    break;

                default:

                    assistantReply =
                        "⚠️ Unknown AI response.";

            }

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: assistantReply
                }
            ]);

        } catch (error) {

            console.error(error);

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content:
                        "❌ Something went wrong while contacting the AI."
                }
            ]);

        }

        setMessage("");

        setLoading(false);

    };

    return (

        <div className="chat-container">

            <div className="chat-header">
                🤖 AI Assistant
                <br />
                <small>
                    Log interaction details using natural language
                </small>
            </div>

            <div className="chat-messages">

                {messages.map((msg, index) => (

                    <div
                        key={index}
                        className={`message ${msg.role}`}
                    >

                        {msg.content}

                    </div>

                ))}

            </div>

            <div className="chat-input">

                <textarea
                    rows="3"
                    placeholder="Describe your interaction with the HCP..."
                    value={message}
                    onChange={(e) =>
                        setMessage(e.target.value)
                    }
                />

                <button
                    onClick={sendMessage}
                    disabled={loading}
                >

                    {loading
                        ? "🤖 AI is analyzing..."
                        : "Send"}

                </button>

            </div>

        </div>

    );

}

export default ChatPanel;