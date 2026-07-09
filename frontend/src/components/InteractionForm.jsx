import { useSelector } from "react-redux";
import "../styles/form.css";
import { saveInteraction } from "../api/interactions";
import { useState } from "react";

function InteractionForm() {

    const interaction = useSelector(
        (state) => state.interaction.data
    );
    const [saving, setSaving] = useState(false);
    const handleSave = async () => {

    try {

        setSaving(true);

        await saveInteraction(interaction);

        alert("Interaction saved successfully!");

    } catch (error) {

        console.error(error);

        alert("Failed to save interaction.");

    } finally {

        setSaving(false);

    }

    };

    return (

        <div className="form-container">

            <div className="form-header">

                <h2>Log Interaction</h2>

                <p>
                    Information extracted by the AI assistant will appear here.
                </p>

            </div>

            <div className="form-grid">

                <FormField
                    label="HCP Name 👨‍⚕️"
                    value={interaction.hcp_name}
                />

                <FormField
                    label="Interaction Type"
                    value={interaction.interaction_type}
                />

                <FormField
                    label="Interaction Date"
                    value={interaction.interaction_date}
                />

                <FormField
                    label="Interaction Time"
                    value={interaction.interaction_time}
                />

                <FormField
                    label="Attendees"
                    value={interaction.attendees}
                />

                <TextAreaField
                    label="Topics Discussed"
                    value={interaction.topics_discussed}
                />

                <TextAreaField
                    label="Materials Shared"
                    value={interaction.materials_shared}
                />

                <TextAreaField
                    label="Summary"
                    value={interaction.summary}
                />

                <FormField
                    label="Sentiment"
                    value={interaction.sentiment}
                />

                <TextAreaField
                    label="Follow Up"
                    value={interaction.follow_up}
                />

            </div>

            <button className="save-btn" onClick={handleSave} disabled={saving}>

                {saving ? "Saving..." : "Save Interaction"}

            </button>

        </div>

    );

}

function FormField({ label, value }) {

    return (

        <div className="field">

            <label>{label}</label>

            <input
                type="text"
                value={value || ""}
                readOnly
            />

        </div>

    );

}

function TextAreaField({ label, value }) {

    return (

        <div className="field full-width">

            <label>{label}</label>

            <textarea
                rows="3"
                value={value || ""}
                readOnly
            />

        </div>

    );

}

export default InteractionForm;