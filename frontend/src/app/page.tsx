export default function HomePage() {
    return (
        <main className="min-h-screen flex items-center justify-center">
            <div className="space-y-4 text-center">
                <h1 className="text-3xl font-bold">AI Trading Assistant</h1>
                <p className="text-gray-600">Login or Register to continue</p>
                <div className="flex gap-4 justify-center">
                    <a className="underline" href="/(auth)/login">Login</a>
                    <a className="underline" href="/(auth)/register">Register</a>
                </div>
            </div>
        </main>
    );
}