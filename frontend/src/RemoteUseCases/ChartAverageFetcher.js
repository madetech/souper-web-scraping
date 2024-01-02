import axios from "axios";

export default async function getChartAverage() {
    const result = await axios.get('/average')
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);
    return result;
}