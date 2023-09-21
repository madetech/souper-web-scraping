import axios from "axios";

export default async function getFeedbackList(id) {
    const result = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/sections/${id}/feedback`)
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);

    return result;
}