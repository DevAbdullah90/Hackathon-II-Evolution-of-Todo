"use client"
import { authClient } from "@/lib/auth-client"
import { useState } from "react"
import { useRouter } from "next/navigation"

export default function SignUpPage() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [name, setName] = useState("")
    const router = useRouter()

    const signUp = async () => {
        await authClient.signUp.email({ 
            email, 
            password, 
            name, 
            callbackURL: "/dashboard"
        }, {
            onRequest: () => {},
            onSuccess: () => router.push("/dashboard"),
            onError: (ctx) => alert(ctx.error.message)
        })
    }

    return (
        <div className="flex flex-col gap-4 p-10 max-w-md mx-auto">
            <h1 className="text-2xl font-bold">Sign Up</h1>
            <input type="text" value={name} onChange={e => setName(e.target.value)} placeholder="Name" className="border p-2" />
            <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" className="border p-2" />
            <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" className="border p-2" />
            <button onClick={signUp} className="bg-green-500 text-white p-2">Sign Up</button>
        </div>
    )
}
