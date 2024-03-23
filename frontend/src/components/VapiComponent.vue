<!--
 Copyright (c) [2024] [The Red Building Group LLC]
 This source code is licensed under the MIT License found in the
 LICENSE file in the root directory of this source tree.
-->

 <template>
  <div class="flex flex-col items-center justify-center">
    <h1 class="text-center text-2xl">Vapi Voice Assistant</h1>
    <button @click="toggleCall" :class="buttonClasses" class="transition-colors duration-200 ease-in-out mt-4 rounded-full w-12 h-12 flex items-center justify-center text-white">
      <template v-if="callStatus === 'active'">
        <!-- Use a 'X' icon for stopping the call -->
        X
      </template>
      <template v-else-if="callStatus === 'loading'">
        <!-- Use a loading icon/spinner -->
        ...
      </template>
      <template v-else>
        <!-- Use a phone icon for starting the call -->
        📞
      </template>
    </button>
    <div v-if="statusMessage" class="mt-4">Status: {{ statusMessage }}</div>
  </div>
</template>

<script>
import Vapi from "@vapi-ai/web";
import systemPrompt from '../assets/systemPrompt.js';

const vapi = new Vapi(process.env.VUE_APP_VAPI_PUBLIC_KEY);

export default {
  name: "VapiComponent",
  data() {
    return {
      vapiInitialized: false,
      statusMessage: "",
      assistantId: null, // Store the assistant ID received from the Vapi API
      callStatus: 'idle', // Possible values: idle, active, loading
    };
  },
  computed: {
    buttonClasses() {
      let baseClasses = 'transition-colors duration-200 ease-in-out mt-4 rounded-full w-12 h-12 flex items-center justify-center text-white';
      if (this.callStatus === 'active') {
        return `${baseClasses} bg-red-500 hover:bg-red-400`;
      } else if (this.callStatus === 'loading') {
        return `${baseClasses} bg-orange-500 hover:bg-orange-400`;
      } else {
        return `${baseClasses} bg-green-500 hover:bg-green-400`;
      }
    }
  },
  methods: {
    async createOrUpdateAssistant() {
      try {
        const response = await fetch(process.env.VUE_APP_POST_URL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            backgroundSound: "off",
            clientMessages: [
              "transcript",
              "hang",
              "speech-update",
              "metadata",
              "conversation-update",
            ],
            dialKeypadFunctionEnabled: false,
            endCallFunctionEnabled: false,
            endCallMessage: "Bye Bye!",
            firstMessage: "Let's talk about work. How may I assist?",
            hipaaEnabled: false,
            llmRequestDelaySeconds: 0.1,
            maxDurationSeconds: 600,
            metadata: {},
            model: {
              maxTokens: 200,
              model: "mixtral-8x7b-32768",
              provider: "groq",
              temperature: 0,
              systemPrompt: systemPrompt,
            },
            name: "AssistantPy2",
            numWordsToInterruptAssistant: 2,
            recordingEnabled: true,
            responseDelaySeconds: 0.4,
            serverUrl: process.env.VUE_APP_SERVERURL,
            serverUrlSecret: process.env.VUE_APP_SERVER_SECRET,
            serverMessages: [
              "end-of-call-report",
            ],
            silenceTimeoutSeconds: 20,
            transcriber: {
              language: "en-US",
              model: "nova-2",
              provider: "deepgram",
            },
            voice: {
              provider: "deepgram",
              voiceId: "luna",
            },
            voicemailDetectionEnabled: false,
          }),
        });

        const data = await response.json();
        if (response.ok) {
          return data;
          // Update UI to reflect success
        } else {
          console.error('Error creating/updating assistant', data);
          this.statusMessage = "Error creating/updating assistant";
          return null;
          // Update UI to show error
        }

      } catch (err) {
        console.error('Failed to create/update assistant', err);
        this.statusMessage = "Failed to create/update assistant";
        return null;
      }
    },
    requestMicrophonePermission() {
      navigator.mediaDevices
        .getUserMedia({ audio: true })
        .then(() => {
          // You now have access to the microphone
        })
        .catch((err) => {
          console.error("Microphone access denied", err);
          this.statusMessage = "Microphone access denied";
        });
    },
    initializeVapi() {
      this.vapiInitialized = true;
      // Listen to Vapi events
      vapi.on("call-start", () => {
        this.statusMessage = "Call has started";
      });
      vapi.on("call-end", () => {
        this.statusMessage = "Call has ended";
      });
      vapi.on("error", (e) => {
        console.error(e);
        this.statusMessage = "An error occurred";
      });
    },
    toggleCall() {
      if (this.callStatus === 'idle' || this.callStatus === 'loading') {
        this.startCall();
      } else if (this.callStatus === 'active') {
        this.stopCall();
      }
    },
    async startCall() {
      this.callStatus = 'loading';
      try {
        // Request microphone permission from the user
        await this.requestMicrophonePermission();

        // Initialize Vapi if not already done
        if (!this.vapiInitialized) {
          this.initializeVapi();
        }

        // Create or update the assistant before starting the call
        const assistantResponse = await this.createOrUpdateAssistant();

        if (assistantResponse && assistantResponse.id) {
          // If we successfully got an assistant ID, start the call with it
          vapi.start(assistantResponse.id); // Use the ID directly
          this.callStatus = 'active';
          this.statusMessage = "Starting call...";
        } else {
          this.callStatus = 'idle';
          this.statusMessage = "Failed to get assistant data.";
        }

      } catch (err) {
        console.error("Error starting call:", err);
        this.statusMessage = "Error starting call";
        this.handleCallError(err);
      }
    },
    stopCall() {
      if (this.vapiInitialized) {
        vapi.stop();
        this.callStatus = 'idle';
        this.statusMessage = "Stopping call...";
      }
    },
  },
  beforeUnmount() {
    if (this.vapiInitialized) {
      vapi.stop(); // Ensure the call is stopped when the component is destroyed
    }
  },
};
</script>
