import axios from "axios";

export default async function getChartCount() {
    const result = await axios.get('/counts')
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);
    return result;
}