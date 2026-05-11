import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 15000
})

export const getHealth = () => apiClient.get('/api/health')

export const uploadImage = (file) => {
  const formData = new FormData()
  formData.append('file', file)

  return apiClient.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

export default apiClient

