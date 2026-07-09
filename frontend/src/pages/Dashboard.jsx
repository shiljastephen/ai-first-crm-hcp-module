import Header from "../components/Header";
import InteractionForm from "../components/InteractionForm";
import ChatPanel from "../components/ChatPanel";

import "../styles/dashboard.css";

function Dashboard() {
    return (
        <>
            <Header />

            <div className="dashboard">

                <div className="left-panel">
                    <InteractionForm />
                </div>

                <div className="right-panel">
                    <ChatPanel />
                </div>

            </div>
        </>
    );
}

export default Dashboard;