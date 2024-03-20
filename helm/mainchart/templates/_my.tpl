{{- define "my-configmap2" -}}
{{- range $key, $value := .Capabilities.APIVersions }}
key: {{ $key }}
APIVersion: {{ $value }}
{{- end }}
{{- end -}}
