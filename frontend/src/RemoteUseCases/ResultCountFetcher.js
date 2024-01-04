import axios from "axios";

export default async function getResultCount() {
    const result = await axios.get('/resultcount')
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);
    return result;
}