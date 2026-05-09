import axios from "axios";

const api = axios.create({ baseURL: "http://localhost:8000" });

export const requestUploadFile = async (file: File) => {
  const formData = new FormData();

  formData.append("file", file);
  try {
    await api.post("/file", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
  } catch (error) {
    console.error(`Network Error: ${error}`);
  }

  try {
    await api.get("/save");
  } catch (error) {
    console.error(`Network Error: ${error}`);
  }
};
