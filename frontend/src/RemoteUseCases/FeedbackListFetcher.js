import axios from "axios";

export default async function getFeedbackList(id) {
    const result = await axios.get(`http://localhost:8000/sections/${id}/feedback`)
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);
    return result;
}