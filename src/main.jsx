import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { i18nReady } from './i18n' // initialize i18next (async, lazy locale loading)

// 초기 언어 번역이 준비된 뒤 렌더하여 번역 깜빡임을 방지한다.
i18nReady.finally(() => {
  createRoot(document.getElementById('root')).render(
    <StrictMode>
      <App />
    </StrictMode>,
  )
})
