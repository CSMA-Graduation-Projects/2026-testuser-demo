import { defineStore } from 'pinia'

export const useDetectionStore = defineStore('detection', {
  state: () => ({
    latestResult: null,
    latestFileName: '',
    loading: false
  }),
  actions: {
    setLoading(status) {
      this.loading = status
    },
    setResult(fileName, result) {
      this.latestFileName = fileName
      this.latestResult = result
    }
  }
})

