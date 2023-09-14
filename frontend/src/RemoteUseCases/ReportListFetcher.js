import axios from "axios";

export default async function getReportList() {
    const result = await axios.get('http://localhost:8081/reports')
    .then(res => res.status === 200 ? res.data.items : res.status)
        .catch(err => err);

    return result;

}