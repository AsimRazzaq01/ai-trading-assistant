# -------------------------
# 1. Builder stage
# -------------------------
FROM node:20-alpine AS builder

WORKDIR /app

# Install deps first (cached layer if package.json/lockfile unchanged)
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./
RUN \
  if [ -f package-lock.json ]; then npm ci; \
  elif [ -f pnpm-lock.yaml ]; then npm install -g pnpm && pnpm install --frozen-lockfile; \
  elif [ -f yarn.lock ]; then yarn install --frozen-lockfile; \
  else npm install; \
  fi

# Copy all project files
COPY . .

# Build Next.js app with standalone output
RUN npm run build

# -------------------------
# 2. Runtime stage
# -------------------------
FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production
# Next.js automatically detects this and optimizes runtime
ENV PORT=3000

# Copy only the built app + runtime deps from builder
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static

# Expose the frontend port
EXPOSE 3000

# Start the Next.js standalone server
CMD ["node", "server.js"]
