
/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
*/

import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Float, MeshDistortMaterial, Sphere, Torus, Stars, Environment, Points, PointMaterial } from '@react-three/drei';
import * as THREE from 'three';

// FIX: Define intrinsic Three.js elements as constants with 'any' type 
// to resolve "Property does not exist on type 'JSX.IntrinsicElements'" errors.
const Group = 'group' as any;
const MeshStandardMaterial = 'meshStandardMaterial' as any;
const AmbientLight = 'ambientLight' as any;
const SpotLight = 'spotLight' as any;

const BrainCore = () => {
  const ref = useRef<THREE.Mesh>(null);
  
  useFrame((state) => {
    if (ref.current) {
      const t = state.clock.getElapsedTime();
      ref.current.rotation.y = t * 0.2;
    }
  });

  return (
    <Sphere ref={ref} args={[1.5, 64, 64]}>
      <MeshDistortMaterial
        color="#D97373"
        envMapIntensity={1}
        clearcoat={0.5}
        metalness={0.5}
        distort={0.4}
        speed={1}
        emissive="#202020"
        emissiveIntensity={0.2}
      />
    </Sphere>
  );
};

const IntentionRings = () => {
  const ref = useRef<THREE.Group>(null);
  
  useFrame((state) => {
    if (ref.current) {
      ref.current.rotation.z += 0.005;
      ref.current.rotation.x += 0.002;
    }
  });

  return (
    // FIX: Using the locally defined Group component
    <Group ref={ref}>
      <Torus args={[3, 0.01, 16, 100]} rotation={[Math.PI / 2, 0, 0]}>
        {/* FIX: Using the locally defined MeshStandardMaterial component */}
        <MeshStandardMaterial color="#202020" transparent opacity={0.2} />
      </Torus>
      <Torus args={[3.5, 0.01, 16, 100]} rotation={[Math.PI / 3, Math.PI / 4, 0]}>
        {/* FIX: Using the locally defined MeshStandardMaterial component */}
        <MeshStandardMaterial color="#D97373" transparent opacity={0.3} />
      </Torus>
    </Group>
  );
}

export const HeroScene: React.FC = () => {
  return (
    <div className="absolute inset-0 z-0 pointer-events-none">
      <Canvas camera={{ position: [0, 0, 10], fov: 45 }} alpha={true}>
        {/* FIX: Using locally defined Light components */}
        <AmbientLight intensity={0.5} />
        <SpotLight position={[10, 10, 10]} intensity={2} color="#D97373" />
        <Float speed={1.5} rotationIntensity={0.5} floatIntensity={0.5}>
          <BrainCore />
          <IntentionRings />
        </Float>
        <Environment preset="studio" />
      </Canvas>
    </div>
  );
};
