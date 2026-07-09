import { createSlice } from "@reduxjs/toolkit";

const initialState = {

    data: {

        hcp_name: "",

        interaction_type: "",

        interaction_date: "",

        interaction_time: "",

        attendees: "",

        topics_discussed: "",

        materials_shared: "",

        summary: "",

        sentiment: "",

        follow_up: ""

    }

};

const interactionSlice = createSlice({

    name: "interaction",

    initialState,

    reducers: {

        setInteraction(state, action) {

            state.data = action.payload;

        },

        clearInteraction(state) {

            state.data = initialState.data;

        }

    }

});

export const {

    setInteraction,

    clearInteraction

} = interactionSlice.actions;

export default interactionSlice.reducer;