import { betterAuth } from "better-auth";
import { Pool } from "pg";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
    database: new Pool({
        connectionString: process.env.DATABASE_URL,
    }),
    emailAndPassword: {
        enabled: true,
    },
    plugins: [
        jwt()
    ],
    session: {
    },
    advanced: {
        cookiePrefix: "taskoo-v2", // Invalidate old opaque cookies
    },
    baseURL: process.env.BETTER_AUTH_URL,
});
