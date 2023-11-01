import axios from "axios";

export default async function getReportList() {
    const result = await axios.get('/reports')
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);
    return result;
}