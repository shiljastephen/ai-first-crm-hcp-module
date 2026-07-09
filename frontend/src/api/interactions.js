import api from "./api";

export const saveInteraction = async (interaction) => {

    const response = await api.post(
        "/interactions/",
        interaction
    );

    return response.data;

};