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
    alert("Error: Could not retrive the Database")
  }

  try {
    await api.get("/save");
  } catch (error) {
    console.error(`Network Error: ${error}`);
    alert("Error: Could not retrive the Database")
  }
};

export const fetchSavedNotes = async () => {
  try {
    const response = await api.get("/notes");
    return response;
  } catch (error) {
    console.error(`Network Error: ${error}`);
    alert("Error: Could not retrive the Database")
  }
};
