<template>
  <div class="page-grid">
    <section class="panel result-banner">
      <div class="panel-header">
        <h4>AI Recognition Result</h4>
        <el-tag :type="riskTagType">{{ riskLabel }}</el-tag>
      </div>
      <template v-if="result">
        <h3>Detection completed for {{ fileName }}</h3>
        <p class="section-copy">
          The backend returned a simulated structured inference payload that can be replaced with a
          real computer vision model in later iterations.
        </p>
      </template>
      <template v-else>
        <h3>No result available yet</h3>
        <p class="section-copy">Upload an image first to generate a demo result.</p>
      </template>
    </section>

    <section class="stats-grid">
      <MetricCard
        label="Person Detection"
        :value="formatBoolean(result?.person_detected)"
        description="Human presence recognition"
      />
      <MetricCard
        label="Truck Detection"
        :value="formatBoolean(result?.truck_detected)"
        description="Heavy vehicle scene monitoring"
      />
      <MetricCard
        label="Risk Level"
        :value="result?.risk_level || 'N/A'"
        description="Rule-based simulated risk output"
      />
      <MetricCard
        label="Confidence"
        :value="result?.confidence || 'N/A'"
        description="Synthetic score for presentation demo"
      />
    </section>

    <section class="panel">
      <div class="panel-header">
        <h4>Structured Payload</h4>
      </div>
      <pre class="result-json">{{ formattedResult }}</pre>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import MetricCard from '@/components/MetricCard.vue'
import { useDetectionStore } from '@/stores/detection'

const store = useDetectionStore()

const result = computed(() => store.latestResult)
const fileName = computed(() => store.latestFileName || 'uploaded image')
const formattedResult = computed(() => JSON.stringify(result.value ?? {}, null, 2))

const riskLabel = computed(() => {
  if (!result.value) {
    return 'Waiting'
  }

  return `Risk: ${result.value.risk_level}`
})

const riskTagType = computed(() => {
  if (!result.value) {
    return 'info'
  }

  return result.value.risk_level === 'high' ? 'danger' : 'success'
})

const formatBoolean = (value) => {
  if (value === true) return 'Detected'
  if (value === false) return 'Not Found'
  return 'N/A'
}
</script>

