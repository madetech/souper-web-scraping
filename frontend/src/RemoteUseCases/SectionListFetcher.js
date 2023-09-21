import axios from "axios";

export default async function getSectionList(id) {
    const result = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/reports/${id}/sections`)
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);
    return result;
}