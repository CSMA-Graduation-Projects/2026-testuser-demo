<template>
  <div class="page-grid">
    <section class="panel upload-panel">
      <div class="panel-header">
        <h4>Image Upload</h4>
        <el-tag type="warning">Demo Inference</el-tag>
      </div>
      <p class="section-copy">
        Select a JPG or PNG image, submit it to the FastAPI interface, and navigate to the result
        page for visualized AI analysis.
      </p>

      <el-upload
        class="upload-box"
        drag
        :auto-upload="false"
        :show-file-list="true"
        :limit="1"
        accept="image/png,image/jpeg"
        :on-change="handleFileChange"
        :on-remove="handleFileRemove"
      >
        <el-icon class="el-icon--upload"><UploadFilled /></el-icon>
        <div class="el-upload__text">Drop image here or <em>click to select</em></div>
        <template #tip>
          <div class="el-upload__tip">Recommended: traffic, campus, or laboratory scene images</div>
        </template>
      </el-upload>

      <div class="hero-actions">
        <el-button
          type="primary"
          size="large"
          :loading="store.loading"
          :disabled="!selectedFile"
          @click="submitUpload"
        >
          Run AI Detection
        </el-button>
        <el-button plain size="large" @click="router.push('/result')">View Last Result</el-button>
      </div>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h4>Current Selection</h4>
      </div>
      <div class="preview-box">
        <template v-if="previewUrl">
          <img :src="previewUrl" alt="preview" class="preview-image" />
        </template>
        <template v-else>
          <p>No image selected yet.</p>
        </template>
      </div>
      <p class="section-copy">{{ selectedFile ? selectedFile.name : 'Please choose an image file.' }}</p>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { UploadFilled } from '@element-plus/icons-vue'
import { uploadImage } from '@/api/client'
import { useDetectionStore } from '@/stores/detection'

const router = useRouter()
const store = useDetectionStore()
const selectedFile = ref(null)
const previewUrl = ref('')

const handleFileChange = (uploadFile) => {
  const rawFile = uploadFile.raw

  if (!rawFile) {
    return
  }

  selectedFile.value = rawFile
  previewUrl.value = URL.createObjectURL(rawFile)
}

const handleFileRemove = () => {
  selectedFile.value = null
  previewUrl.value = ''
}

const submitUpload = async () => {
  if (!selectedFile.value) {
    ElMessage.warning('Please select an image first.')
    return
  }

  store.setLoading(true)

  try {
    const { data } = await uploadImage(selectedFile.value)
    store.setResult(selectedFile.value.name, data.result)
    ElMessage.success(data.message)
    router.push('/result')
  } catch (error) {
    ElMessage.error('Upload failed. Please confirm the backend service is running.')
  } finally {
    store.setLoading(false)
  }
}
</script>

