{{- define "my-configmap-label" -}}
# Environment
clusterEnv: {{ .Values.global.clusterEnv }}
namespace: {{ .Values.global.namespace }}
{{- end -}}
