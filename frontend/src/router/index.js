import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/DashboardView.vue'
import UploadView from '@/views/UploadView.vue'
import ResultView from '@/views/ResultView.vue'
import AboutView from '@/views/AboutView.vue'

const routes = [
  { path: '/', name: 'dashboard', component: DashboardView, meta: { title: 'Dashboard' } },
  { path: '/upload', name: 'upload', component: UploadView, meta: { title: 'Image Upload' } },
  { path: '/result', name: 'result', component: ResultView, meta: { title: 'AI Result' } },
  { path: '/about', name: 'about', component: AboutView, meta: { title: 'System Intro' } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

