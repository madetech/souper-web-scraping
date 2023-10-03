import axios from "axios";

export default async function runScrape() {
    const result = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/scrape`)
        .then(res => res.status)
        .catch(err => err);
    return result;
}
