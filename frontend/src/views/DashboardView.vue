<template>
  <div class="page-grid">
    <section class="hero-panel">
      <p class="eyebrow">Graduation Project Showcase</p>
      <h3>Present your AI detection workflow with a clean, modern, and deployable system.</h3>
      <p class="section-copy">
        This template connects a Vue 3 front end to a FastAPI back end, supports image upload,
        returns simulated AI recognition results, and is suitable for live defense demos.
      </p>
      <div class="hero-actions">
        <el-button type="primary" size="large" @click="router.push('/upload')">
          Start Demo
        </el-button>
        <el-button plain size="large" @click="router.push('/about')">Architecture</el-button>
      </div>
    </section>

    <section class="stats-grid">
      <MetricCard label="Front End" value="Vue 3 + Vite" description="Fast, modular SPA delivery" />
      <MetricCard label="UI Layer" value="Element Plus" description="Professional component system" />
      <MetricCard label="Back End" value="FastAPI" description="Typed API service and deployment ready" />
      <MetricCard label="Demo Mode" value="AI Vision" description="Image upload and risk evaluation" />
    </section>

    <section class="panel">
      <div class="panel-header">
        <h4>Workflow Overview</h4>
        <el-tag type="info">4 Steps</el-tag>
      </div>
      <el-steps :active="4" finish-status="success" simple>
        <el-step title="Upload image" />
        <el-step title="Send to API" />
        <el-step title="Generate result" />
        <el-step title="Visualize analysis" />
      </el-steps>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h4>Service Status</h4>
        <el-button text @click="fetchHealth">Refresh</el-button>
      </div>
      <div class="status-box" :class="{ online: health.ok, offline: !health.ok }">
        <span class="status-dot"></span>
        <div>
          <strong>{{ health.ok ? 'Backend Ready' : 'Backend Unreachable' }}</strong>
          <p>{{ health.message }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, reactive } from 'vue'
import { useRouter } from 'vue-router'
import MetricCard from '@/components/MetricCard.vue'
import { getHealth } from '@/api/client'

const router = useRouter()

const health = reactive({
  ok: false,
  message: 'Checking API connection...'
})

const fetchHealth = async () => {
  health.ok = false
  health.message = 'Checking API connection...'

  try {
    const { data } = await getHealth()
    health.ok = data.status === 'ok'
    health.message = `${data.message} | version ${data.version}`
  } catch (error) {
    health.ok = false
    health.message = 'Unable to connect to FastAPI service. Start the backend first.'
  }
}

onMounted(fetchHealth)
</script>

