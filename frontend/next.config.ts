import type { NextConfig } from "next";
import process from "next/dist/build/webpack/loaders/resolve-url-loader/lib/postcss";

const nextConfig: NextConfig = {
    // Strict mode helps catch potential problems early
    reactStrictMode: true,

    // Output standalone build (better for Docker)
    output: "standalone",

    // Ensure server actions work in Next.js 15
    experimental: {
        serverActions: {
            // Allow calls from your local frontend in dev
            allowedOrigins: ["localhost:3000"],
        },
    },

    // Enable cross-origin fetch if you deploy backend separately
    async headers() {
        return [
            {
                source: "/(.*)",
                headers: [
                    { key: "Access-Control-Allow-Origin", value: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000" },
                    { key: "Access-Control-Allow-Credentials", value: "true" },
                ],
            },
        ];
    },
};

export default nextConfig;
