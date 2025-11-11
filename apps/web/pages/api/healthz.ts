import type { NextApiRequest, NextApiResponse } from 'next';

type HealthResponse = {
  ok: boolean;
  service: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<HealthResponse>
) {
  res.status(200).json({ ok: true, service: 'web' });
}
