import { useState } from "react";
import api from "../services/api";

function UploadForm() {
    const [file, setFile] = useState(null);
    const [jobDescription, setJobDescription] = useState("");
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!file) {
            alert("Please upload a resume.");
            return;
        }

        if (!jobDescription.trim()) {
            alert("Please enter a job description.");
            return;
        }

        const formData = new FormData();

        formData.append("file", file);
        formData.append("job_description", jobDescription);

        try {
            setLoading(true);

            const response = await api.post("/analyze", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });

            console.log("Backend Response:");
            console.log(response.data);

            setResult(response.data);

        } catch (error) {
            console.error("Full Error:", error);

            if (error.response) {
                console.log("Response Data:", error.response.data);
                console.log("Status:", error.response.status);
                alert(JSON.stringify(error.response.data));
            } else {
                alert(error.message);
            }

        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-4xl mx-auto mt-10 px-4">

            {/* HEADER */}
            <div className="text-center mb-10">

                <h1 className="text-4xl font-bold">
                    🤖 AI Resume Analyzer
                </h1>

                <p className="text-gray-600 mt-3">
                    Analyze your resume against a job description
                    using NLP and Machine Learning.
                </p>

            </div>


            {/* UPLOAD CARD */}
            <div className="bg-white shadow-lg rounded-xl p-8">

                <form onSubmit={handleSubmit}>

                    {/* RESUME UPLOAD */}

                    <label className="block font-semibold mb-2">
                        Upload Resume
                    </label>

                    <input
                        type="file"
                        accept=".pdf"
                        onChange={(e) => setFile(e.target.files[0])}
                        className="border p-3 rounded-lg w-full mb-6"
                    />

                    {file && (
                        <p className="text-sm text-gray-600 mb-6">
                            Selected file: {file.name}
                        </p>
                    )}


                    {/* JOB DESCRIPTION */}

                    <label className="block font-semibold mb-2">
                        Job Description
                    </label>

                    <textarea
                        rows="8"
                        className="border rounded-lg w-full p-3"
                        value={jobDescription}
                        onChange={(e) =>
                            setJobDescription(e.target.value)
                        }
                        placeholder="Paste the job description here..."
                    />


                    {/* BUTTON */}

                    <button
                        type="submit"
                        disabled={loading}
                        className="mt-6 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-6 py-3 rounded-lg font-semibold"
                    >
                        {loading
                            ? "Analyzing Resume..."
                            : "Analyze Resume"}
                    </button>

                </form>

            </div>


            {/* RESULTS */}

            {result && !result.error && (

                <div className="mt-10">

                    <h2 className="text-3xl font-bold mb-6">
                        Analysis Result
                    </h2>


                    {/* SCORE CARDS */}

                    <div className="grid md:grid-cols-2 gap-6">

                        {/* MATCH SCORE */}

                        <div className="bg-white shadow-lg rounded-xl p-6 text-center">

                            <p className="text-gray-500">
                                Resume Match
                            </p>

                            <p className="text-4xl font-bold text-blue-600 mt-2">
                                {result.match_score}%
                            </p>

                        </div>


                        {/* ATS SCORE */}

                        <div className="bg-white shadow-lg rounded-xl p-6 text-center">

                            <p className="text-gray-500">
                                ATS Score
                            </p>

                            <p className="text-4xl font-bold text-green-600 mt-2">
                                {result.ats_score}%
                            </p>

                        </div>

                    </div>


                    {/* SKILLS */}

                    <div className="grid md:grid-cols-2 gap-6 mt-6">


                        {/* RESUME SKILLS */}

                        <div className="bg-white shadow-lg rounded-xl p-6">

                            <h3 className="text-xl font-bold mb-4">
                                ✅ Resume Skills
                            </h3>

                            <div className="flex flex-wrap gap-2">

                                {result.resume_skills.map(
                                    (skill, index) => (

                                        <span
                                            key={index}
                                            className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full"
                                        >
                                            {skill}
                                        </span>

                                    )
                                )}

                            </div>

                        </div>


                        {/* MISSING SKILLS */}

                        <div className="bg-white shadow-lg rounded-xl p-6">

                            <h3 className="text-xl font-bold mb-4">
                                ⚠️ Missing Skills
                            </h3>

                            <div className="flex flex-wrap gap-2">

                                {result.missing_skills.length > 0 ? (

                                    result.missing_skills.map(
                                        (skill, index) => (

                                            <span
                                                key={index}
                                                className="bg-red-100 text-red-700 px-3 py-1 rounded-full"
                                            >
                                                {skill}
                                            </span>

                                        )
                                    )

                                ) : (

                                    <p className="text-green-600">
                                        No missing skills 🎉
                                    </p>

                                )}

                            </div>

                        </div>

                    </div>


                    {/* ATS BREAKDOWN */}

                    <div className="bg-white shadow-lg rounded-xl p-6 mt-6">

                        <h3 className="text-xl font-bold mb-6">
                            ATS Breakdown
                        </h3>

                        {Object.entries(
                            result.ats_breakdown
                        ).map(([key, value]) => (

                            <div
                                key={key}
                                className="mb-5"
                            >

                                <div className="flex justify-between mb-1">

                                    <span className="capitalize">
                                        {key.replace("_", " ")}
                                    </span>

                                    <span className="font-semibold">
                                        {value}
                                    </span>

                                </div>

                                <div className="bg-gray-200 rounded-full h-3">

                                    <div
                                        className="bg-blue-600 h-3 rounded-full"
                                        style={{
                                            width: `${value}%`
                                        }}
                                    />

                                </div>

                            </div>

                        ))}

                    </div>

                </div>

            )}


            {/* ERROR */}

            {result?.error && (

                <div className="mt-6 bg-red-100 text-red-700 p-4 rounded-lg">

                    {result.error}

                </div>

            )}

        </div>
    );
}

export default UploadForm;