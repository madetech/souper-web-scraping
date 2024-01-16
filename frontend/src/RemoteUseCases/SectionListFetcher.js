import axios from "axios";

export default async function getSectionList(id) {
    const result = await axios.get(`/reports/${id}/sections`)
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => {
            console.error("Axios error:", err);
            return err});
    return result;
}