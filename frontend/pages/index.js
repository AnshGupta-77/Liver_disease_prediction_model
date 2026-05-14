import { useState } from 'react'

export default function Home() {
  const [formData, setFormData] = useState({
    age: '',
    gender: 'Male',
    total_bilirubin: '',
    direct_bilirubin: '',
    alkaline_phosphotase: '',
    alamine_aminotransferase: '',
    aspartate_aminotransferase: '',
    total_protiens: '',
    albumin: '',
    albumin_and_globulin_ratio: ''
  })

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [result, setResult] = useState(null)

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch('http://localhost:8000/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          age: parseInt(formData.age),
          gender: formData.gender,
          total_bilirubin: parseFloat(formData.total_bilirubin),
          direct_bilirubin: parseFloat(formData.direct_bilirubin),
          alkaline_phosphotase: parseInt(formData.alkaline_phosphotase),
          alamine_aminotransferase: parseInt(formData.alamine_aminotransferase),
          aspartate_aminotransferase: parseInt(formData.aspartate_aminotransferase),
          total_protiens: parseFloat(formData.total_protiens),
          albumin: parseFloat(formData.albumin),
          albumin_and_globulin_ratio: parseFloat(formData.albumin_and_globulin_ratio)
        })
      })

      if (!response.ok) {
        throw new Error('Failed to get prediction')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message || 'An error occurred during prediction')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-medical-50 to-white">
      <div className="max-w-4xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Liver Disease Prediction
          </h1>
          <p className="text-gray-600">
            Enter patient medical data to predict liver disease likelihood
          </p>
        </div>

        {/* Form */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Age */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Age (years)
                </label>
                <input
                  type="number"
                  name="age"
                  value={formData.age}
                  onChange={handleChange}
                  required
                  min="0"
                  max="120"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter age"
                />
              </div>

              {/* Gender */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Gender
                </label>
                <select
                  name="gender"
                  value={formData.gender}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                >
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
              </div>

              {/* Total Bilirubin */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Total Bilirubin (mg/dL)
                </label>
                <input
                  type="number"
                  step="0.1"
                  name="total_bilirubin"
                  value={formData.total_bilirubin}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>

              {/* Direct Bilirubin */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Direct Bilirubin (mg/dL)
                </label>
                <input
                  type="number"
                  step="0.1"
                  name="direct_bilirubin"
                  value={formData.direct_bilirubin}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>

              {/* Alkaline Phosphotase */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Alkaline Phosphotase (IU/L)
                </label>
                <input
                  type="number"
                  name="alkaline_phosphotase"
                  value={formData.alkaline_phosphotase}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>

              {/* Alamine Aminotransferase */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Alamine Aminotransferase (IU/L)
                </label>
                <input
                  type="number"
                  name="alamine_aminotransferase"
                  value={formData.alamine_aminotransferase}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>

              {/* Aspartate Aminotransferase */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Aspartate Aminotransferase (IU/L)
                </label>
                <input
                  type="number"
                  name="aspartate_aminotransferase"
                  value={formData.aspartate_aminotransferase}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>

              {/* Total Proteins */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Total Proteins (g/dL)
                </label>
                <input
                  type="number"
                  step="0.1"
                  name="total_protiens"
                  value={formData.total_protiens}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>

              {/* Albumin */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Albumin (g/dL)
                </label>
                <input
                  type="number"
                  step="0.1"
                  name="albumin"
                  value={formData.albumin}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>

              {/* Albumin and Globulin Ratio */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Albumin and Globulin Ratio
                </label>
                <input
                  type="number"
                  step="0.1"
                  name="albumin_and_globulin_ratio"
                  value={formData.albumin_and_globulin_ratio}
                  onChange={handleChange}
                  required
                  min="0"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-medical-500 focus:border-medical-500"
                  placeholder="Enter value"
                />
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-medical-600 text-white py-3 px-4 rounded-md hover:bg-medical-700 focus:ring-2 focus:ring-medical-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? 'Analyzing...' : 'Predict Liver Disease'}
            </button>
          </form>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
            <p className="text-red-800">{error}</p>
          </div>
        )}

        {/* Result Card */}
        {result && (
          <div className={`bg-white rounded-lg shadow-md p-6 ${
            result.prediction === 1 ? 'border-l-4 border-red-500' : 'border-l-4 border-green-500'
          }`}>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-2xl font-bold text-gray-900">
                Prediction Result
              </h2>
              <div className={`px-4 py-2 rounded-full text-sm font-medium ${
                result.prediction === 1 
                  ? 'bg-red-100 text-red-800' 
                  : 'bg-green-100 text-green-800'
              }`}>
                {result.prediction === 1 ? 'High Risk' : 'Low Risk'}
              </div>
            </div>

            <p className="text-lg text-gray-700 mb-4">
              {result.message}
            </p>

            <div className="bg-gray-50 rounded-lg p-4">
              <div className="flex items-center justify-between">
                <span className="text-gray-600">Confidence Score</span>
                <span className="text-2xl font-bold text-medical-600">
                  {(result.confidence * 100).toFixed(1)}%
                </span>
              </div>
              <div className="mt-2 bg-gray-200 rounded-full h-2">
                <div
                  className={`h-2 rounded-full transition-all duration-500 ${
                    result.prediction === 1 ? 'bg-red-500' : 'bg-green-500'
                  }`}
                  style={{ width: `${result.confidence * 100}%` }}
                />
              </div>
            </div>

            <p className="text-sm text-gray-500 mt-4">
              * This prediction is for informational purposes only and should not replace professional medical diagnosis.
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
